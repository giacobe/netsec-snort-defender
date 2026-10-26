SNORT COMMUNITY RULES LAB

1. Verify the archive with sha256sum -c community-rules-snort2-retrieved-2026-10-26.sha256
2. Extract it into a working directory.
3. Inspect and search community-rules/community.rules.
4. Copy only the applicable official rule into /etc/snort/rules/local.rules.
5. Test the configuration with snort -T -c /etc/snort/snort.conf -i eth0.

The archive is an unmodified Snort 2 community-rules download. See
COMMUNITY-RULES-SOURCE.txt and the license files inside the archive.
