% Torque Calculation for Exoskeleton Elbow Joint
% Author: Abhishek Tyagi

% Parameters
mass = 10;             % kg - weight lifted
g = 9.81;              % m/s^2 - gravity
distance = 0.35;       % m - from elbow to load

% Torque Calculation
force = mass * g;
torque = force * distance;

fprintf('Required Torque: %.2f Nm\n', torque);
