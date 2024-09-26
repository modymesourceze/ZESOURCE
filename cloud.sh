#!/usr/bin/env bash

cat <<'EOF'
$$$$$$$$\    $$$$$\ $$\                           
\____$$  |   $$  __|$$|                          
    $$  /    $$ |______
   $$  /     $$$$$\ $$\
  $$  /      $$  _____|
 $$  /       $$ |
 $$$$$$$$\   $$$$$\$$$| 
\________|   \________/
                                                  
                                                  
                                                  
Copyright (C) 2020-2024 by modymesourceze@Github, < https://github.com/modymesourceze >.
This file is part of < https://github.com/modymesourceze/ZESOURCE > project,
and is released under the "GNU v3.0 License Agreement".
Please see < https://github.com/modymesourceze/ZESOURCE/blob/SourceZe/LICENSE >
All rights reserved.
EOF

gunicorn app:app --daemon && python -m SourceZe
