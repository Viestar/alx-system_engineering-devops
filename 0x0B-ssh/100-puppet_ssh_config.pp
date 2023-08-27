# client SSH configuration file so that you can connect to a server without typing a password
file { '/home/Viestar/.ssh/config':
  ensure  => present,
  mode    => '0600',
  content => "
    Host 34.237.91.110
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ",
}
