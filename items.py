

files = {
    '/etc/xinetd.d/tftp': {
        'mode': '755',
        'content_type': 'jinja2',
        'triggers': [
            "svc_systemd:xinetd:restart"
        ],
    }
}
