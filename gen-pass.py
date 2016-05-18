#!/usr/bin/env python
'''
Copyright (C) 2015-Present Juan Espinoza. All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

	1. Redistributions of source code must retain the above copyright notice,
	this list of conditions and the following disclaimer.
	2. Redistributions in binary form must reproduce the above copyright notice,
	this list of conditions and the following disclaimer in the documentation
	and/or other materials provided with the distribution.
	3. Neither the name of the copyright holder nor the names of its
	contributors may be used to endorse or promote products derived from this
	software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import random
import click
import string
import time

@click.command()
@click.option("-p", default=1,
              help="Number of passwords to generate. One password by\
              default.")
@click.option("-l", default=8,
              help="Password length. Ten characters by default.")
@click.option("-s", is_flag=True,
              help="Include special characters (punctuations). Excluded by\
              default.")
@click.option("-n", is_flag=True, help="Numbers only password. Ideal for PINs.")

def gen_pass(p, l, s, n):
    ''' Random password generator. '''
    pass_dict = dict(zip(['length', 'passwords', 'special', 'numonly'], 
                        [l, p, s, n]))
    my_pw = list()

    if pass_dict['numonly']:
        # Generate numeric only password
        chars = string.digits
    elif pass_dict['special']:
        # Generate password containing alphanumeric and punctuations.
        chars = string.ascii_lowercase + string.ascii_uppercase + \
                string.digits + string.punctuation
    else:
        # Generate alphanumeric password.
        chars = string.ascii_lowercase + string.ascii_uppercase + \
                string.digits

    for _ in xrange(pass_dict['passwords']):
        my_pw.append([
            ''.join(random.SystemRandom(time.time()).choice(chars)
                    for _ in xrange(pass_dict['length']))
            ])

    # Print password to console.
    print '\n'.join(''.join(elems) for elems in my_pw)

if __name__ == '__main__':
    gen_pass()
