#include<stdio.h>
void PrintArray(int pInt[], int size);
void MergeSort(int *arr, int lower, int upper, int size);


int main(){

    printf("Anish Bhattacharya\t170111037\n");
    int size, i, a[100],b[100];
    printf("Enter size of the array : ");
    scanf("%d", &size);
    printf("Enter elements : ");
    for (i = 0; i < size; i++)
        scanf("%d", &a[i]);
    printf("\n==Before Sorting==\n");
    PrintArray(a, size);
    MergeSort(a,0,size-1,size);
    printf("\n==After Sorting==\n");
    PrintArray(a, size);
    return 1;
}

void PrintArray(int pInt[100], int size) {
    for (int i = 0; i < size; i++)
        printf("%d  ", pInt[i]);
}

void MergeSort(int *arr, int lower, int upper, int size){
    int b[100],first[100],second[100],k=0,i=lower;
    int mid = lower+(upper-lower)/2;
    int j = mid+1;
    if(lower==upper)
        return;
    else{
        MergeSort(arr,lower,mid,size);
        MergeSort(arr,mid+1,upper,size);
        while(i<=mid && j<=upper){
            if(arr[i]<=arr[j])
                b[k++]=arr[i++];
            else
                b[k++]=arr[j++];}
            if(i>mid){
                while(j<=upper)
                    b[k++]=arr[j++];
            }
            else{
                while(i<=mid)
                b[k++]=arr[i++];}
        k=0;
        for(i=lower;i<=upper;i++)
            arr[i]=b[k++];
    }

}
