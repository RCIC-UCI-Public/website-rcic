% Distribute iterations to multiple workers
% in a parallel pool on a single node

% open the default local cluster profile for a single node job
p = parcluster('local');

% number of workers for the pool
nworkers = str2double(getenv('SLURM_NTASKS'));

% open the parallel pool, recording the time it takes
tic;
parpool(p, nworkers); 
fprintf('Opening the parallel pool took %g seconds.\n', toc)

% here run your algorithm

% integer factorization example is from  
% https://www.mathworks.com/help/parallel-computing/scale-up-from-desktop-to-cluster.html
primeNumbers = primes(uint64(2^8));
compositeNumbers = primeNumbers.*primeNumbers(randperm(numel(primeNumbers)));
factors = zeros(numel(primeNumbers),2);

% run on the pool of workers
tic;
parfor idx = 1:numel(compositeNumbers)
    factors(idx,:) = factor(compositeNumbers(idx));
end
elapsedTime = toc;

% print result matrix and time it took to calculate
factors
fprintf('Calculation took %g seconds.\n', elapsedTime)

% close the parallel pool and exit
delete(gcp); 
exit
