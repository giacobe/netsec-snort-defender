# netsec-snort-defender

Root filesystem overlay for the defender in the PolyLab three-stage Snort
exercise.

The overlay initializes the PolyLinux exercise identity, serves benign HTTP
endpoints, includes a pinned Snort 2 community-rules archive, generates the
scenario-specific threat-intelligence bulletin, and provides `labctl`.

This repository is payload input for `buildroot-builder2` script 03. Package it
against the `snort-defender` baseline with:

```sh
scripts/03-package-payload.sh \
  --baseline artifacts/<snort-defender-artifact> \
  --repo https://github.com/giacobe/netsec-snort-defender \
  --ref main \
  --payload-subdir rootfs-overlay \
  --archive-dest / \
  --permissions-file permissions.txt \
  --output-prefix packaged-defender \
  --output packaged \
  --force
```

`permissions.txt` records the required ownership and Unix modes. Verify the
payload bytes on Linux with:

Verify on Linux with:

```sh
sha256sum -c SHA256SUMS
```

This payload repository is deliberately independent of the script 02 Buildroot
baseline configuration.
