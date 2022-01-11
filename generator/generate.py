#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import json

try:
    from dns import resolver, rdatatype
except ImportError:
    print("We need dnspython, use pip install")


def resolve(qname, rdtype):
    try:
        ans = resolver.resolve(qname, rdtype)
        for rdata in ans:
            return rdata.to_text()
        return ans
    except resolver.NoAnswer:
        return False


class SiteGroup:
    """Collection of sites"""

    list = []

    def handlesitefile(self, file):
        print("Checking file: %s" % file)
        site = file.stem
        print("  Checking site: %s" % site)
        with file.open() as f:
            data = json.load(f)
            sdata = {}
            sdata["site"] = site
            sdata["url"] = "%s://%s/" % (data["protocol"], site)
            sdata["description"] = data["description"]
            sdata["protocol"] = data["protocol"]
            # TODO validate A and AAAA records
            rr_a = resolve(site, rdatatype.A)
            if rr_a:
                print(
                    "::warning,title=Has A::%s Got unexpected answer for A %s"
                    % (site, rr_a)
                )
                return
            rr_aaaa = resolve(site, rdatatype.AAAA)
            print("::notice,title=Has AAAA::%s : %s" % (site, rr_aaaa))
            print(sdata)
            self.list.append(sdata)

    def walksites(self, jsonpath):
        for f in jsonpath.glob("*.json"):
            if f.is_file():
                self.handlesitefile(f)

    def sort(self):
        self.list.sort(key=lambda site: site["site"])


if __name__ == "__main__":
    sitegroup = SiteGroup()
    sitegroup.walksites(Path("./sites/"))
    sitegroup.sort()

    outfile = Path("./_data/v6onlysites.json")
    with outfile.open("w") as f:
        json.dump(sitegroup.list, f, indent=4)
