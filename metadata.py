defaults = {}
if node.has_bundle("apt"):
    defaults = {
        'apt': {
            'packages': {
                'update-inetd': {'installed': True},
                'tftpd': {
                    'installed': True,
                    'needs': [
                        'pkg_apt:update-inetd',
                    ]
                },
            }
        }
    }


@metadata_reactor
def add_iptables_rules(metadata):
    if not node.has_bundle("iptables"):
        raise DoNotRunAgain

    interfaces = ['main_interface']
    interfaces += metadata.get('tftp/additional_interfaces', [])

    iptables_rules = {}
    for interface in interfaces:
        iptables_rules += repo.libs.iptables.accept(). \
            input(interface). \
            state_new(). \
            udp(). \
            dest_port(69)

    return iptables_rules


@metadata_reactor
def add_restic_rules(metadata):
    if not node.has_bundle('restic'):
        raise DoNotRunAgain

    return {
        'restic': {
            'backup_folders': [metadata.get('tftp/root', '/srv/tftp/'), ],
        }
    }
