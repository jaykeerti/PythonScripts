import requests
import sys
import os
import threading

def download_naruto(val):
        print("Task  "+str(val)+"assigned to thread: {}".format(threading.current_thread().name))
        print("ID of process running task "+str(val)+": {}".format(os.getpid()))
        link = "http://streamcdnuservi4api.ml/nrt/N360Sub/Naruto_"+str(val)+"_Subbed_Naruto360.com.mp4"
        file_name = "Naruto_"+str(val)+"_Subbed_Naruto360.com.mp4"
        #Directory to store naruto Episodes
        with open("E:\\Naruto\\"+file_name, "wb") as f:
                print("Downloading %s" % file_name)
                response = requests.get(link, stream=True)
                total_length = response.headers.get('content-length')

                if total_length is None: # no content length header
                    f.write(response.content)
                else:
                    dl = 0
                    total_length = int(total_length)
                    for data in response.iter_content(chunk_size=4096):
                        dl += len(data)
                        f.write(data)
                        done = int(50 * dl / total_length)
                        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
                        sys.stdout.flush()


if __name__ == "__main__":
    threads=[]
    #please insert the range of episodes you need like 1-10 --->(for i in range(1,10))
    for i in range(200,220):
        thread = threading.Thread(target=download_naruto, name='t1', args=(i,))
        # t2 = threading.Thread(target=download_naruto, name='t2', args=(39,))
        threads.append(thread)
        #starting threads
        thread.start()
        # t2.start()
        # wait until all threads finish
        # thread.join()
        # t2.join()

















