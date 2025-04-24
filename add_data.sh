JSON=(
    '{"name": "Earth", "description": "blue planet", "moons_n": 1}'
    '{"name": "Mercury", "description": "grey planet", "moons_n": 0}'
    '{"name": "Venus", "description": "golden brown planet", "moons_n": 0}'
    '{"name": "Mars","description": "red planet","moons_n": 2}'
    '{"name": "Jupiter", "description": "yellow, brown, red planet","moons_n": 79}'
    '{"name": "Saturn","description": "yellow, brown, grey planet", "moons_n": 62}'
    '{"name": "Uranus","description": "cyan planet", "moons_n": 27}'
    '{"name": "Neptune", "description": "blue","moons_n": 14}'
)

for planet in "${JSON[@]}"
do
curl --header "Content-Type: application/json" \
--request POST \
--data $planet \
http://localhost:5000/planets
done