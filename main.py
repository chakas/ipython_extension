from IPython.core.magic import Magics, line_magic, magics_class
from simple_salesforce import Salesforce
import pandas as pd

@magics_class
class SfMagics(Magics):
    
    def login_into_sf(self,username,password,token,url):
		sf = Salesforce(username=username,password=password,security_token=token,instance=url,sandbox=True)
		# data = sf.query("select id,lastname from contact limit 1000")
		ns = self.shell.user_ns
		ns['sfObject'] = sf

    @line_magic
    def sflogin(self, line='', setup='pass'):
    	opts, stmt = self.parse_options(line, 'u:p:t:l', posix=False,strict=False)
    	try:
    		self.login_into_sf(opts["u"], opts["p"], opts["t"],opts["l"])
    	except Exception as e:
    		print str(e)


    @line_magic
    def sf_query(self,query):
    	data = self.shell.user_ns['sfObject'].query(query)
    	df =  pd.DataFrame.from_dict(data['records'])
    	df = df.drop('attributes',axis=1)
    	return df

if __name__ == '__main__':
    ip = get_ipython()
    ip.register_magics(SfMagics)
    try:
    	from sys import modules
    	pandas_module = modules['pandas']
    	# pandas_module.read_sf = SfMagics.read_salesforce
    except KeyError, e:
    	print "Please load pandas into environment"


    # globals()['pd'].read_sf = SfMagics().read_salesforce
