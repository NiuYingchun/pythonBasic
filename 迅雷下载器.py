from multiprocessing import Pool
import time

def down_load(movie_name):
    for i in range(5):
        print('电影：{}，下载进度{}%'.format(movie_name,(i / 4 * 100)))
        time.sleep(1)
        return movie_name

def alert(movie_name):
    print('恭喜{}下载完成了。。。'.format(movie_name))


if __name__ == '__main__':
    movie_lst = ['西红柿首富','功夫小子','功夫熊猫','叶问','功夫','战郎','红海行动']
    pool = Pool(3)
    for movie_name in movie_lst:
        pool.apply_async(down_load,(movie_name,),callback=alert)

    pool.close()
    pool.join()