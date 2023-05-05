# Configurating Nginx

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider  => shell,
  command   => 'sudo apt-get -y install nginx',
  before    => Exec['start Nginx'],
}

exec {'create first directory':
  provider  => shell,
  command   => 'sudo mkdir -p /data/web_static/releases/test/',
  before    => Exec['create second directory'],
}

exec
