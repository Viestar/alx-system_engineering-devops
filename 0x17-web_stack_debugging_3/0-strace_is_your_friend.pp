# Puppet Script that Fixes a wordpress site running on apache2
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; sudo systemctl restart apache2.service',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
} 
