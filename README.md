# cobalt playlist downloader
a lot of people have been asking for this, so i made it. paste the link, download the first file, allow multiple file downloads if you didn't do that before and keep saving files until it finishes.

for now it only supports audio because it was made to download music, i think???

## supported services
- yourtube <!-- no, don't visit, it was flagged as an 18+ website when i visited it in school because it was mentioned in vlc and no, it's still not fixed -->

## api
if you want you can use the `/getvideos` endpoint.
example curl command:
```
curl https://playlist.spawn.best/getvideos?playlist=(playlist url)
```
example response:
```
https://youtube.com/watch?v=EpSRlZTh0U8;https://youtube.com/watch?v=q9Bu6BZbuQ8;https://youtube.com/watch?v=V0n8guxv5kc;https://youtube.com/watch?v=cImU2y7IB3A;https://youtube.com/watch?v=h2WygHkAyT4;https://youtube.com/watch?v=OX8BPatGT5Q;https://youtube.com/watch?v=Oyyx6BhyDtM;https://youtube.com/watch?v=D2gqTLaXPVk;https://youtube.com/watch?v=S3yHQoy_zEw;https://youtube.com/watch?v=tC-TZX0AAck;https://youtube.com/watch?v=LbPYygtpxJk;https://youtube.com/watch?v=YHxj8I8YnB0
```
video links are seperated by semicolons <!-- (gd colon reference? (his second channel name (gd semicolon (but without the gd (also with an s at the end (also hi person that looks at source code (hi (hi (and once again (hi)! (why am i wasting my time writing this) (idk)) (of commit history) (probably commit (history (((())))))))))))) (probably not)) -->

## to-do list
**features**
- [ ] add video support
**services**
- [ ] add tiktok support
- [ ] add soundcloud support
- [ ] add bilibili support
      wip: [`support/bilibili` branch](https://github.com/ihatespawn/playlist/tree/support/bilibili)