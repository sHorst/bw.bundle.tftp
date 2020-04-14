

files = {
    '/etc/xinetd.d/tftp': {
        'mode': '755',
        'content_type': 'jinja2',
        'triggers': [
            "svc_systemd:xinetd:restart"
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
