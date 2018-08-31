#include<stdio.h>

int main(void) {

    int st_len = 64;
    int x;

    scanf("%d",&x);
    int i = 1;
    int tmp = st_len/2;

    while (st_len > x) {
        /*st_len += tmp;
        st_len -= tmp;
        */
        i++;

        if ((st_len - tmp) >= x) {
            st_len -= tmp;
            i--;
        }

        tmp = tmp/2;

    }

    printf("%d",i);

    return 0;
}
