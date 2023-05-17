#version 330 core

out vec4 final_colors;
in vec4 vertex_colors;

void main() {
    final_colors = vertex_colors;
}
