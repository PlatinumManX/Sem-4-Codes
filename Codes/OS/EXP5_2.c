#include<stdio.h>

int findLRU(int time[], int n) {
    int pos = 0;
    for (int i = 1; i < n; ++i)
        if (time[i] < time[pos])
            pos = i;
    return pos;
}

void lruPageReplacement(int pages[], int n, int frames) {
    int frame[frames], time[frames], counter = 0, pageFaults = 0, pageHits = 0;
    for (int i = 0; i < frames; ++i)
        frame[i] = -1;
    
    for (int i = 0; i < n; ++i) {
        int flag = 0;
        for (int j = 0; j < frames; ++j) {
            if (frame[j] == pages[i]) {
                time[j] = ++counter;
                pageHits++;
                printf("\nPage %d hit", pages[i]);
                flag = 1;
                break;
            }
        }
        
        if (!flag) {
            int pos = -1;
            for (int j = 0; j < frames; ++j) {
                if (frame[j] == -1) {
                    pos = j;
                    break;
                }
            }
            if (pos == -1)
                pos = findLRU(time, frames);
            
            frame[pos] = pages[i];
            time[pos] = ++counter;
            pageFaults++;
        }
        
        printf("\nFrames: ");
        for (int j = 0; j < frames; ++j)
            printf("%d ", frame[j] == -1 ? -1 : frame[j]);
    }
    
    printf("\nTotal Page Faults: %d\nTotal Page Hits: %d\n", pageFaults, pageHits);
}

int main() {
    int n, frames;
    printf("********************LRU***********************");
    printf("\nEnter the number of pages: ");
    scanf("%d", &n);
    int pages[n];
    printf("Enter the reference string: ");
    for (int i = 0; i < n; ++i)
        scanf("%d", &pages[i]);
    printf("Enter the number of frames: ");
    scanf("%d", &frames);
    
    lruPageReplacement(pages, n, frames);
    return 0;
}
