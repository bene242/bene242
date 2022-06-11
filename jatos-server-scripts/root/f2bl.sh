#!/bin/bash
/usr/bin/rsync -a /var/log/fail2ban* /home/bene/fail2ban/
/bin/chown -R bene.users /home/bene/fail2ban/
