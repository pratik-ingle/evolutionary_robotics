
import os
import shutil
import neat
import visualize


# The current working directory
local_dir = os.path.dirname(__file__)

# The directory to store outputs
out_dir = os.path.join(local_dir, 'out')

xor_inputs =  [(0.0,0.0), (0.0,1.0),(1.0,0.0), (1.0,1.0)]
xor_outputs = [(0.0,), (1.0,), (1.0,), (0.0,)]

def eval_fitness(net):
    error_sum = 0.0
    for xi, xo in zip(xor_inputs, xor_outputs):
        output = net.activate(xi)
        error_sum +=  abs(xo[0] - output[0])
    fitness = (4- error_sum) ** 2
    return fitness


def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 4.0
        net = neat.nn.FeedForwardNetwork.create(genome=genome, config= config)
        genome.fitness = eval_fitness(net=net)
        
        
def run_experiment(config_file):   
    config = neat.Config(neat.DefaultGenome,
                        neat.DefaultReproduction,
                        neat.DefaultSpeciesSet,
                        neat.DefaultStagnation,
                        config_file)
    p = neat.Population(config=config)
    
    
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5, filename_prefix= 'out/neat-checkpoint-'))
    
    best_genome = p.run(eval_genomes, 200)
    
    # Display the best genome among generations.
    print('\nBest genome:\n{!s}'.format(best_genome))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    net = neat.nn.FeedForwardNetwork.create(best_genome, config)
    for xi, xo in zip(xor_inputs, xor_outputs):
        output = net.activate(xi)
        print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))
    
    best_genome_fitness = eval_fitness(net=net)
    if best_genome_fitness > config.fitness_threshold:
        print("\n\nSUCESS: The XOR problem solver found!!!")
    else:
        print("\n\nFAILURE: Failed to find XOR problem solver!!!")
        
    node_names = {-1:'A', -2:'B', 0:'A XOR B'}
    visualize.draw_net(config, best_genome, True,  node_names= node_names, directory=out_dir)
    visualize.plot_stats(stats, ylog=False, view=True, filename=os.path.join(out_dir, 'avg_fitness.svg'))
    visualize.plot_species(stats, view=True, filename=os.path.join(out_dir, 'speciation.svg'))


def clean_output():
    if os.path.isdir(out_dir):
        # remove files from previous run
        shutil.rmtree(out_dir)

    # create the output directory
    os.makedirs(out_dir, exist_ok=False)


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    config_path = os.path.join(local_dir, 'xor_config.ini')

    # Clean results of previous run if any or init the ouput directory
    clean_output()

    # Run the experiment
    run_experiment(config_path)