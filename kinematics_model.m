% Forward Kinematics for 2-Link Planar Arm
% Author: Abhishek Tyagi

% Link lengths
l1 = 0.3;  % m
l2 = 0.25; % m

% Joint angles (in radians)
theta1 = pi/4;
theta2 = pi/6;

% Forward Kinematics
x = l1*cos(theta1) + l2*cos(theta1 + theta2);
y = l1*sin(theta1) + l2*sin(theta1 + theta2);

fprintf('Wrist Position: x = %.2f m, y = %.2f m\n', x, y);
