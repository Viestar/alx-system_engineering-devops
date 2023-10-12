# Puppet Script that Fixes a wordpress site running on apache2
$config_file = '/var/www/html/wp-settings.php'

exec { 'edit_file':
  command => "sed -i 's/phpp/php/g' ${config_file}",
  path    => ['/bin','/usr/bin']
}
