import numpy as np

cross = np.cross

# 18th April, 2018
# Related Matlab Code: Desktop\mat-workspace\MatlabCode-UR

w=[[0 0 1], [1 0 0], [1 0 0], [1 0 0], [0 0 1], [0 1 0]];
q=[[0 0 0], [0 0 0], [0 0 5], [0 4 5], [0 4 7], [0 5 7]];


ksai = []
ksai.append( [cross(-w[i],q[i]), w[i]] )

for i=1:dof
   ksai(:,i)=[cross(-w(i,:)',q(i,:)'); w(i,:)']; # Notice that the symbol of w is miuns (-w)
end

for i=1:dof
    ksai_wan{i}=se3(ksai(:,i));
end

gst0=[eye(3) q(end,:)'; 0 0 0 1]; # Keep the posture of end-effctor same with base coordination.

effector_gst=gst0*effector;



% gst_6=@(theta)(expm(ksai_wan{1}*theta(1))*...
%     expm(ksai_wan{2}*theta(2))*  expm(ksai_wan{3}*theta(3))*  expm(ksai_wan{4}*theta(4))*...
%     expm(ksai_wan{5}*theta(5))* expm(ksai_wan{6}*theta(6))* gst0);


