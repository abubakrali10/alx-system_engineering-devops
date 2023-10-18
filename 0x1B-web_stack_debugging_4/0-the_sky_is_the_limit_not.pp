# up the limit of nginx requests
exec { 'nginx-fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

# restart nginx server
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}