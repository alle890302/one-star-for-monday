"""One Star for Monday — make.fun entry.

Final line (19 words, 106 chars, one line, no trailing newline):
    One star. Monday sat me down at 9am, served meetings instead of coffee,
    and still hasn't brought the bill.

Judge criteria (in order): (1) one-star review of Monday as a restaurant;
(2) real diner's complaint — table/server/dish/bill gone wrong; (3) the joke
is Monday-specific; (4) short and quotable; (5) plain text, <=25 words.

Revision passes:
- Pass 1 (kept): the line above. Monday is the waiter/restaurant itself:
  sat down at 9am (table), served meetings instead of coffee (the dish is
  wrong), and the bill never comes (you can never leave Monday). The punch
  lands in the last clause; "meetings instead of coffee" is a Monday-only
  swap — no other weekday gets reviewed this way.
- Pass 2 (challenger, rejected): "One star. Monday's special is a cold
  inbox, a warm laptop, and a waiter who reads the specials for ninety
  minutes." (21 words, 114 chars, verified). Rejected: it has a dish (the special)
  and a waiter, but no table and no bill, so it scores weaker on criterion
  2; and its punch ("reads the specials for ninety minutes") is a slower,
  punnier turn than "still hasn't brought the bill", so it loses on
  criterion 4 (quotable, punch lands cleanly). The Monday-meeting image is
  good, but the kept line covers the same ground with a full restaurant
  structure.
"""
import os

ENTRY = ("One star. Monday sat me down at 9am, served meetings instead of "
         "coffee, and still hasn't brought the bill.")

assert 1 <= len(ENTRY) <= 180, f"char count {len(ENTRY)} outside 1-180 gate"
assert len(ENTRY.split()) <= 25, f"word count {len(ENTRY.split())} over 25"
assert "\n" not in ENTRY

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
