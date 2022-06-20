#!/bin/bash

solution_command=$(history | tail -n 1 | cut -d" " -f5-)

cat << EOF > ./solution_script.sh
#!/bin/bash
${solution_command}

EOF

chmod +x solution_script.sh

./solution_script.sh > flag.txt