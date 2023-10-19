# Enable holberton user to open a file without any error message, 'increase-hard-limt':, 'increase-soft-limit':

exec { 'increase-hard-limt':
        command => "/bin/sed -i /etc/security/limits.conf -e 's/hard nofile [0-9]\+/hard nofile 97816/g'"
}

exec { 'increase-soft-limit':
        command => "/bin/sed -i /etc/security/limits.conf -e 's/soft nofile [0-9]\+/soft nofile 97816/g'"
}
