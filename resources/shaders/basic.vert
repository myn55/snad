#version 330 core

layout(location = 0) in vec2 position;
layout(location = 1) in vec4 colors;
out vec4 vertex_colors;

uniform mat4 projection;

void main() {
    gl_Position = projection * vec4(position, 0, 1);
    vertex_colors = colors;
}