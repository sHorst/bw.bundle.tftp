@metadata_processor
def add_apt_packages(metadata):
    if node.has_bundle("apt"):
        metadata.setdefault('apt', {})
        metadata['apt'].setdefault('packages', {})

        metadata['apt']['packages']['update-inetd'] = {
            'installed': True,
        }
        metadata['apt']['packages']['tftpd'] = {
            'installed': True,
            'needs': [
                'pkg_apt:update-inetd',
            ]
        }

    return metadata, DONE


@metadata_processor
def add_iptables_rules(metadata):
    if node.has_bundle("iptables"):
        interfaces = ['main_interface']
        interfaces += metadata.get('tftp', {}).get('additional_interfaces', [])

        for interface in interfaces:
            metadata += repo.libs.iptables.accept(). \
                input(interface). \
                state_new(). \
                udp(). \
                dest_port(69)

    return metadata, DONE


@metadata_processor
def add_restic_rules(metadata):
    if node.has_bundle('restic'):
        metadata.setdefault('restic', {})
        metadata['restic']['backup_folders'] = metadata['restic'].get('backup_folders', []) + [metadata.get('tftp', {}).get('root', '/srv/tftp/'), ]

    return metadata, DONE
