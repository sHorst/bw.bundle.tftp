from bundlewrap.exceptions import BundleError

if not node.has_bundle('xinetd'):
    raise BundleError('you need to have xinetd enabled for this node')


files = {
    '/etc/xinetd.d/tftp': {
        'mode': '755',
        'content_type': 'jinja2',
        'triggers': [
            "svc_systemd:xinetd.service:restart"
        ],
    }
}

tftp_root = node.metadata.get('tftp', {}).get('root', '/srv/tftp/').rstrip('/')

directories = {
    node.metadata.get('tftp', {}).get('root', '/srv/tftp/').rstrip('/'): {
        'mode': '755',
        'owner': 'root',
        'group': 'root',
    },
}
