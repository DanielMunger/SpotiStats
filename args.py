#!/usr/bin/env python
import argparse
import sys

parser = argparse.ArgumentParser(description="AWS S3 management utility")
parser.set_defaults(func=None)
subparsers = parser.add_subparsers()



spotparse = subparsers.add_parser('spotify')
# encrypt_parser = subparsers.add_parser('encrypt')



# encrypt_parser.set_defaults(func='encrypt')

# encrypt_parser.add_argument('-b', '--bucket', required=True,
                            # help='S3 Bucket')
                            
spotparse.set_defaults(func='set_defaults')
spotparse.add_argument('-u','--username', required=True, help='User to authenticate')

# encrypt_parser.add_argument('--prefix', default='',
#                             help='s3 bucket prefix used for filtering objects to encrypt')
# encrypt_parser.add_argument('--sse', default='aws:kms',
#                             help='s3 server side encryption algorithm AES256|aws:kms')
# encrypt_parser.add_argument('--kms-key-id', default=None, required=True, #TODO: revisit requirement
#                             help='kms key id used for encryption, must be in the form of an arn')
# encrypt_parser.add_argument('--region', default='us-west-2', help='aws region')
# encrypt_parser.add_argument('--profile', help='aws profile')
# encrypt_parser.add_argument('--dryrun', action='store_true',
#                             help="print actions to be taken without executing them")
# encrypt_parser.add_argument('--debug', action='store_true',
#                             help="log debug messages")
# encrypt_parser.add_argument('--quiet', action='store_true',
#                             help="don't print status updates, only finishing stats")

args = parser.parse_args(sys.argv[1:])

if args.func == None:
    parser.print_help()
    quit()

print(args)
