# Kills a killmenow process

exec {'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/',
}
