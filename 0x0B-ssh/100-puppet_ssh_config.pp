# client SSH configuration file so that you can connect to a server without typing a password
file { '/home/your_username/.ssh/config':
  ensure  => present,
  owner   => 'your_username',
  group   => 'your_group',
  mode    => '0600',
  content => "
    Host your_server_ip_here
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ",
}
