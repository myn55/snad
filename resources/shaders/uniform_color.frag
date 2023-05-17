#version 330 core

out vec4 final_color;

uniform vec4 user_color;

void main() {
    final_color = user_color;
}