#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct node{
  int key;
  struct node *left, *right;
} node_t;

void insert(node_t **tree, int val){
    node_t *temp = NULL;
    if(!(*tree)){
      temp = (node_t *)malloc(sizeof(node_t));
      temp->left = temp->right = NULL;
      temp->key = val;
      *tree = temp;
      return;
    }
    if(val < (*tree)->key){
      insert(&(*tree)->left, val);
    }
    else if(val > (*tree)->key){
      insert(&(*tree)->right, val);
    }
}

void print_preorder(node_t *tree){
  if (tree){
    printf("%d\n",tree->key);
    print_preorder(tree->left);
    print_preorder(tree->right);
  }
}

void print_inorder(node_t *tree){
  if (tree){
    print_inorder(tree->left);
    printf("%d\n",tree->key);
    print_inorder(tree->right);
  }
}

void print_postorder(node_t *tree){
  if (tree){
    print_postorder(tree->left);
    print_postorder(tree->right);
    printf("%d\n",tree->key);
  }
}

int main(){
  node_t *root;
  root = NULL;
  char s[100];
  FILE *f;
  f = fopen("file.txt", "r");
  if(f == NULL){
    printf("Failed to open file.\n");
    return -1;
  }
  while(fscanf(f, "%s", s) != EOF){
    insert(&root, atoi(s));
  }
  printf("Preorder:\n");
  print_preorder(root);
  printf("Inorder:\n");
  print_inorder(root);
  printf("Postorder:\n");
  print_postorder(root);
  fclose(f);
  return 0;
}
