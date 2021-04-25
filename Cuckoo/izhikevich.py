def izhikevich(Weights,Time,Features): 
  C=100; vr=-60; vt=-40; k=0.7; 
  a=0.03; b=-2; c=-50; d=100; 
  vpeak=35; 

  tau=1; 
  n=round(Time/tau); 
  v=vr*ones(1,n); u=0*v; 
  spikes=0;
  gamma = 100;

  I = gamma*sum(Features*Weights);
  
  for i in range(1, n-1):
    v(i+1)=v(i)+tau*(k*(v(i)-vr)*(v(i)-vt)-u(i)+I)/C;
    u(i+1)=u(i)+tau*a*(b*(v(i)-vr)-u(i));
    
    if v(i+1)>=vpeak:
      v(i)=vpeak;
      v(i+1)=c;
      u(i+1)=u(i+1)+d;
      spikes=spikes+1;
      
  return spikes
