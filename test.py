import unittest
from mainfunc import maintest

class MyTest(unittest.TestCase):

    orig = 'C:\image\sim_0.8\orig.txt'
    folderpath = 'C:\image\sim_0.8\\'

    # 测试文件不存在
    def test_fileNotFound(self):
        try:
            fileName = "orig_0.8_bai.txt"
            cosValue = maintest.calCos(self.orig, self.folderpath+fileName)
            print(fileName+"的相似度为:"+format(cosValue, ".3f"))
        except Exception as e:
            print(e)    

    # def test_add(self):
    #     fileName = "orig_0.8_add.txt"
    #     cosValue = maintest.calCos(self.orig, self.folderpath+fileName)
    #     print(fileName+"的相似度为:"+format(cosValue, ".3f"))

    # def test_del(self):
    #     fileName = "orig_0.8_del.txt"
    #     cosValue = maintest.calCos(self.orig, self.folderpath+fileName)
    #     print(fileName+"的相似度为:"+format(cosValue, ".3f"))

    # def test_dis_1(self):
    #     fileName = "orig_0.8_dis_1.txt"
    #     cosValue = maintest.calCos(self.orig, self.folderpath+fileName)
    #     print(fileName+"的相似度为:"+format(cosValue, ".3f"))

    # def test_dis_3(self):
    #     fileName = "orig_0.8_dis_3.txt"
    #     cosValue = maintest.calCos(self.orig, self.folderpath+fileName)
    #     print(fileName+"的相似度为:"+format(cosValue, ".3f"))

    # def test_dis_7(self):
    #     fileName = "orig_0.8_dis_7.txt"
    #     cosValue = maintest.calCos(self.orig, self.folderpath+fileName)
    #     print(fileName+"的相似度为:"+format(cosValue, ".3f"))

    # def test_dis_10(self):
    #     fileName = "orig_0.8_dis_10.txt"
    #     cosValue = maintest.calCos(self.orig, self.folderpath+fileName)
    #     print(fileName+"的相似度为:"+format(cosValue, ".3f"))

    # def test_dis_15(self):
    #     fileName = "orig_0.8_dis_15.txt"
    #     cosValue = maintest.calCos(self.orig, self.folderpath+fileName)
    #     print(fileName+"的相似度为:"+format(cosValue, ".3f"))

    # def test_mix(self):
    #     fileName = "orig_0.8_mix.txt"
    #     cosValue = maintest.calCos(self.orig, self.folderpath+fileName)
    #     print(fileName+"的相似度为:"+format(cosValue, ".3f"))

    # def test_rep(self):
    #     fileName = "orig_0.8_rep.txt"
    #     cosValue = maintest.calCos(self.orig, self.folderpath+fileName)
    #     print(fileName+"的相似度为:"+format(cosValue, ".3f"))


if __name__ == "__main__":
    unittest.main()