#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// Define a structure for linked list nodes
struct Node {
    int vertex;
    struct Node* next;
};

// Create a new node with the given vertex
struct Node* createNode(int vertex) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->vertex = vertex;
    newNode->next = NULL;
    return newNode;
}

int main() {
    int vertices;
    scanf("%d", &vertices);

    if (vertices == 0) {
        printf("-1\n");
        return 0;
    }

    if (vertices == 1) {
        int v;
        scanf("%d", &v);
        printf("%d\n", v);
        return 0;
    }

    // Create an array of linked lists for the adjacency list representation
    struct Node* adjList[vertices];

    for (int i = 0; i < vertices; i++) {
        adjList[i] = NULL; // Initialize each adjacency list as empty
    }

    int vertex;

    while (1) {
        int v_i, v_j;
        int count = scanf("%d %d", &v_i, &v_j);

        if (count == 1) {
            vertex = v_i;
            break;
        } else {
            // Add edge to the adjacency list
            struct Node* newNode = createNode(v_j);
            newNode->next = adjList[v_i - 1];
            adjList[v_i - 1] = newNode;
        }
    }

    // Traverse the adjacency list to find adjacent vertices
    int vertex_list[vertices];
    int count = 0;

    struct Node* current = adjList[vertex - 1];
    while (current != NULL) {
        vertex_list[count] = current->vertex;
        current = current->next;
        count++;
    }

    printf("%d\n", count);

    for (int i = count-1; i >= 0; i--) {
        if (i == 0) {
            printf("%d\n", vertex_list[i]);
        } else {
            printf("%d,", vertex_list[i]);
        }
    }

    return 0;
}
