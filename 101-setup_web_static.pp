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

exec {'create second directory':
  provider  => shell,
  command   => 'sudo mkdir -p /data/web_static/shared/',
  before    => Exec['content into html'],
}

exec {'symbolic':
   provider => shell,
   command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
   before   => Exec['put location']
}

exec {'put location':
    provider => shell,
    command  => 'sudo sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-available/default',
    before => Exec['restart Nginx'],
}

file {'/data/':
   ensure => directory,
   owner  => 'ubuntu',
   group  => 'ubuntu',
}
