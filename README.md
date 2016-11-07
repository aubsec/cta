# cta.py
###https://github.com/aubsec/cta.git

## Requirements
1.  Python 3
2.  Modify "cta_config.conf" with API keys.
3.  Set appropriate sections in "cta_config.conf" to Enable = True.

## Usage

cta.py requries at least one argument of -s.

|Argument   |Description|
|---        |---|
|-c, --config |Optional. Specify a configuration file.  Defaults to cta_config.conf.|
|-s, --string |Required. Specify a string or file of strings to search.|
|-h, --help | Displays this help message and exits.|


Typical Usage:

Example 1:  cta.py -s 0d1ef429ed4a31753e5905e5356ba94d

Example 2:  cta.py -s file.txt

## ToDo
- [ ] Parse arguments.
- [ ] Parse configuration file.
- [ ] Execute code based on options in configuration file.
- [ ] User input of single MD5 Hash
- [ ] User input of MD5 hash list
- [ ] ThreatGrid search using user defined API key.
- [ ] CSV formatted output to stdout.
- [ ] Fully commented.
- [ ] Error handling.

## Credits

Matthew Aubert
- @aubsec
- aubsec@gmail.com
- github.com/aubsec
- aubsec.github.io

## License

cta.py is a tool for doing automated seraches of string values from various 
threat intelligence sources.

Copyright (C) 2016 Matthew Aubert

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.
