#!/usr/bin/env bash
# Author: @lontivero

CMD=${*}
PORT=${PORT-9051}
ADDRESS=${ADDRESS-127.0.0.1}
CMD_WITH_AUTH="AUTHENTICATE\r\n${CMD}\r\nQUIT"

echo -e $CMD_WITH_AUTH | nc $ADDRESS $PORT