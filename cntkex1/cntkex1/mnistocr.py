import cntk as C
from cntk.io import MinibatchSource, CTFDeserializer, StreamDef, StreamDefs
from cntk.ops import relu, element_times, constant
from cntk.layers import Dense 
from cntk.learners import learning_rate_schedule, UnitType, adadelta
from cntk import cross_entropy_with_softmax, classification_error, Trainer 
from cntk.logging import ProgressPrinter


#define network 
input_dim = 784
num_output_classes = 10
hidden_layers_dim = 200


feature = C.input_variable(input_dim)
label = C.input_variable(num_output_classes)

scaled_input = element_times(constant(0.00390625), feature)

#define network topology

h1 = Dense(hidden_layers_dim, activation=relu)(scaled_input)
h2 = Dense(hidden_layers_dim, activation=relu)(h1)
z = Dense(num_output_classes, activation=None)(h2)

#define loss and error functions
ce = cross_entropy_with_softmax(z, label)
pe = classification_error(z, label)


#Data source for training and testing
path_train = "D:/MachineLearning/CNTK-2.0/Examples/Image/DataSets/MNIST/Train-28x28_cntk_text.txt"
path_test = "D:/MachineLearning/CNTK-2.0/Examples/Image/DataSets/MNIST/Test-28x28_cntk_text.txt"

#train model
reader_train = MinibatchSource(CTFDeserializer(path_train, StreamDefs(
        features=StreamDef(field='features', shape=input_dim),
        labels=StreamDef(field='labels', shape=num_output_classes))))

input_map = {
        feature: reader_train.streams.features,
        label: reader_train.streams.labels
    }

#Instantiate progress writers
num_sweeps_to_train_with = 10
progress_writers = [ProgressPrinter(
    tag='Training',
    num_epochs=num_sweeps_to_train_with)]

#schedule learning rate
lr = learning_rate_schedule(1, UnitType.sample)

#define trainer object
trainer = Trainer(z, (ce, pe), [adadelta(z.parameters, lr)], progress_writers)

#define training session
minibatch_size = 64
num_samples_per_sweep = 60000
num_sweeps_to_train_with = 10
C.training_session(
        trainer=trainer,
        mb_source=reader_train,
        mb_size=minibatch_size,
        model_inputs_to_streams=input_map,
        max_samples=num_samples_per_sweep * num_sweeps_to_train_with,
        progress_frequency=num_samples_per_sweep
    ).train()


#test model
reader_test = MinibatchSource(CTFDeserializer(path_test, StreamDefs(
        features=StreamDef(field='features', shape=input_dim),
        labels=StreamDef(field='labels', shape=num_output_classes))))

input_test_map = {
        feature: reader_test.streams.features,
        label: reader_test.streams.labels
    }

test_minibatch_size = 1024
num_samples = 10000
num_minibatches_to_test = num_samples / test_minibatch_size
test_result = 0.0

for i in range(0, int(num_minibatches_to_test)):
    mb = reader_test.next_minibatch(test_minibatch_size, input_map=input_test_map)
    eval_error = trainer.test_minibatch(mb)
    test_result = test_result + eval_error
    print("Test error:", eval_error, test_result)

print("Average Test error:", test_result/num_minibatches_to_test)


