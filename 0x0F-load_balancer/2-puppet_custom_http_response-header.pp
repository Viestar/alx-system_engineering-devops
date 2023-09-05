# puppet manifest creating a custom HTTP header response
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

#  Making nginx is installed.
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

# Altering default_server to direct to a new link
file_line { 'a':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require => Package['nginx'],
}

# Adding hostname into the header.
file_line { 'b':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

# Pasting Best school into index.html
file { '/var/www/html/index.html':
  content => 'Holberton School',
  require => Package['nginx'],
}

# MAking sure he server is running.
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
