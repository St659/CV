from Meth_Blue_Glucose_12_10_16 import plot_cv, cv_difference
import matplotlib.pyplot as plt
plt.style.use(['seaborn-white', 'seaborn-notebook'])


def main():
   plot_difference()
   
def plot_difference():
    meth04_directory = "/Users/st659/Google Drive/Meth Blue 4-10-16"
    meth12_directory = "/Users/st659/Google Drive/Meth Blue Glucose 12-10-16"

    meth4_diff = cv_difference(meth04_directory)
    meth12_diff = cv_difference(meth12_directory)
    
    figure = plt.figure()
    axe = figure.add_subplot(111)
    axe.errorbar(meth4_diff[0], meth4_diff[1], meth4_diff[2], label= 'bw')
    axe.errorbar(meth4_diff[0], meth4_diff[3], meth4_diff[4], label = 'pk')
    axe.errorbar(meth12_diff[0], meth12_diff[1], meth12_diff[2], label= 'bw glu')
    axe.errorbar(meth12_diff[0], meth12_diff[3], meth12_diff[4], label = 'pk glu')
    plt.legend(loc = 'upper right')
    figure2 = plt.figure()

    axe2 = figure2.add_subplot(111)
    axe2.plot(meth4_diff[0], meth4_diff[1], label = 'bw')
    axe2.plot(meth4_diff[0],meth4_diff[3], label = 'pk')
    axe2.plot(meth12_diff[0],meth12_diff[1], label = 'bw glu')
    axe2.plot(meth12_diff[0],meth12_diff[3], label = 'pk glu')

    plt.legend(loc = 'upper right')
    plt.show()
   
def plot_variance():
    meth04_directory = "/Users/st659/Google Drive/Meth Blue 4-10-16"
    meth12_directory = "/Users/st659/Google Drive/Meth Blue Glucose 12-10-16"

    meth4_var = plot_cv(meth04_directory)
    meth12_var = plot_cv(meth12_directory)

    fig = plt.figure()
    axe = fig.add_subplot(111)
    axe.plot(meth4_var[0], meth4_var[1], label='MB BW')
    axe.plot(meth4_var[0], meth4_var[2], label='MB PK')
    axe.plot(meth12_var[0], meth12_var[1], label='MB Glu BW')
    axe.plot(meth12_var[0], meth12_var[2], label='MB Glu PK')
    plt.legend(loc= 'upper right')
    plt.show()


if __name__ == '__main__':
    main()