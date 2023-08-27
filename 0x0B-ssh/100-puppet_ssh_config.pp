# configuration ssh config using puppet

file {'etc/ssh/ssh_config':
  ensure  => present,
  content => "
		# This is the ssh client system-wide configuration file.
		Host *
		PasswordAuthentication no
		IdentityFile ~/.ssh/school",
}
