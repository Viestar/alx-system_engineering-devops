# kill_process.pp

# Define the exec resource to kill the process
exec { 'killmenow':
  command     => '/usr/bin/pkill killmenow',  # Replace with the actual process name
  path        => ['/bin', '/usr/bin'],        # Specify search paths for the command
  user        => 'root',                      # User to run the command as
  refreshonly => true,                        # Only run when explicitly refreshed
}