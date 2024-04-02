% An example "Hello World" code for illustration how to
% parallelize MatLab processes across a single node with 
% a pool of workers.

% open the default local cluster profile for a single node job
p = parcluster('local');

% number of workers for the pool
nworkers = str2double(getenv('SLURM_NTASKS'));

% open the parallel pool, recording the time it takes
tic;
parpool(p, nworkers);
fprintf('Opening the parallel pool took %g seconds.\n', toc)

% "single program multiple data"
spmd
    fprintf('Worker %d says Hello World!\n', labindex)
end

% close the parallel pool and exit
delete(gcp);
exit
