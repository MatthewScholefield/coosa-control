# Coosa Control

*Control script for coosa smart plugs*

This repo contains a script to control COOSA smart plugs

## Usage

Install with:

```bash
pip3 install coosa-control --user
```

Configure by extracting the TCP data sent to your local device for the on and off commands by using a tool like [Packet Capture](https://play.google.com/store/apps/details?id=app.greyshirts.sslcapture) while triggering the plug with its official app. Then, save this data into files like `enable-command.dat` or `disable-command.dat` and pass it to the script:

```bash
coosa-control --save-params --enable-data enable-command.dat --disable-data disable-command.dat --ip-address 192.168.0.14
```

Finally, use with:

```bash
coosa-control on
coosa-control off
```
