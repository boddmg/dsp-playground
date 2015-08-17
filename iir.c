// x,y,Na,a,Nb,b,y_i
float32 sum = 0;

int j =0, k=0;
for(j=0;j<=Nb-1; ++j)
{
	if(i >= j)
	{
		sum += b[j]*x[i-j];
	}
}

for (int k = 1; i =< Na-1; ++i)
{
	if (i >= k)
	{
		sum -= a[k] * y[i-k];
	}
}

y_i = sum / a[0];